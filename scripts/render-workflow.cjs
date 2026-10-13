// Optional artwork build tool. No dependency is needed to use the writing skill.
const fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require(process.env.WORKFLOW_PLAYWRIGHT || 'playwright');
const root=path.resolve(__dirname,'..');
const output=path.resolve(process.argv.find(a=>a.startsWith('--out='))?.slice(6)||path.join(root,'build','workflow'));
const keysOnly=process.argv.includes('--keyframes-only');
const source=path.join(root,'assets','workflow','source.html');
const times=[0,5,9,10.6,14,16,19,21,25,29,33,38];
fs.mkdirSync(output,{recursive:true});
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.WORKFLOW_BROWSER?{executablePath:process.env.WORKFLOW_BROWSER}:{})});
 const checks=[];
 for(const [layout,width,height] of [['desktop',1120,800],['mobile',640,1180]]){
  const p=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
  await p.goto(pathToFileURL(source).href+'?capture=1&layout='+layout);
  await p.evaluate(()=>document.fonts.ready);
  const dir=path.join(output,layout);fs.mkdirSync(dir,{recursive:true});
  for(const t of times){
   await p.evaluate(({t,layout})=>workflow.draw(t,layout),{t,layout});
   const check=await p.evaluate(()=>({ ...lastFrame, overflow:[...document.querySelectorAll('svg text')].map(e=>({text:e.textContent,b:e.getBBox()})).filter(e=>e.b.x<0||e.b.y<0||e.b.x+e.b.width>lastFrame.width||e.b.y+e.b.height>lastFrame.height).map(e=>e.text)}));
   if(check.overflow.length||check.lastTextBaseline>check.paperBottom-10)throw new Error(JSON.stringify(check));
   checks.push(check);
   await p.screenshot({path:path.join(dir,'key-'+String(t).replace('.','_')+'.png')});
  }
  await p.evaluate(({layout})=>workflow.draw(38,layout),{layout});
  // Keep word spacing stable when a viewer uses a different system font fallback.
  await p.locator('svg text').evaluateAll(es=>es.forEach(e=>{
   e.setAttribute('textLength',e.getComputedTextLength());
   e.setAttribute('lengthAdjust','spacingAndGlyphs');
  }));
  fs.writeFileSync(path.join(root,'assets','workflow',layout+'-still.svg'),(await p.locator('svg').evaluate(e=>e.outerHTML)).replaceAll('><','>\n<')+'\n');
  if(!keysOnly){
   const frameDir=path.join(dir,'frames');fs.mkdirSync(frameDir,{recursive:true});
   // 80 ms per frame is exactly representable in GIF's 10 ms time units.
   for(let frame=0;frame<525;frame++){
    await p.evaluate(({t,layout})=>workflow.draw(t,layout),{t:frame*.08,layout});
    await p.screenshot({path:path.join(frameDir,String(frame).padStart(4,'0')+'.png')});
   }
  }
  console.log('Rendered '+layout+(keysOnly?' keyframes':' frames and keyframes'));
  await p.close();
 }
 await browser.close();
 fs.writeFileSync(path.join(output,'layout-checks.json'),JSON.stringify(checks,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
