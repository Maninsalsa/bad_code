

Here's a comprehensive list of all performance tips quoted verbatim from the text:

**What Makes Apps Slow:**
1. "Loading too much stuff... bringing too much stuff to the party you're carrying all this stuff you can't get through the door"
2. "Slow database work... if you're not using them correctly you don't have indexes set up properly or you're not doing performant queries"
3. "Slow server... if the server that you're making requests to are slow they're slow to respond"
4. "Waterfall requests... one request renders and realizes it needs something else and then that thing renders and realizes it needs something else"

**Solutions:**

**Caching:**
- "Client side caching... caches it in your browser and you set client side caching by giving a caching headers"
- "Server side caching where you can cache things in memory or you can cach them in a key store... redis is one of the most popular ways"
- "Local data... you can store data in your index DB you can store data in local storage or even in cookies"

**Images:**
- "The easiest way to have images be fast is to use a service uh like cloudinary"
- "Install the imagebot extension and what it will do is every time you add an image to your git repo it'll just crawl for any images"
- "Ship less... less images"
- "Maybe you're shipping an image when something could be SVG that loads just fine"
- "Maybe you could just straight up do it in CSS"

**CSS & JavaScript:**
- "Inlining critical CSS"
- "Put preload and prefetch tags either in the head of your document"
- "Pre-loading on Hover... you hover over a link and it starts loading that page behind the scenes"
- "Ship less code... there are browser apis that do many of the things that you might be shipping a library for"
- "Opt for smaller or tree shaken packages over large bundled uh big monolithic libraries"

**SVG Icons:**
- "The fastest smallest way to do this if you have an icons is an SVG Sprite sheet using symbols"
- "Use an app called nucleus o app.com"

**Fonts:**
- "Variable fonts are incredible but you do need to know specifically if you need one variation of that font"
- "You can load a font and only tell it which letters you want"
- "If you don't need custom fonts... just load up the system fonts"
- "If you're just using uh you know regular non-bold whatever non-italicized body font then loading a variable for that font is going to be a much larger font load than just the static font"

**Infrastructure:**
- "Use a CDN... make sure your content is distributed globally"
- "Turn on gzip... your server will send your data HTML CSS JavaScript anything back as a compressed stream"
- "Throw Cloud flare on top of anything"

**Streaming:**
- "Supporting streaming... if you have one little piece of your website that is slow... your whole website shouldn't have to wait just for that that one component"
- "In react it's called a suspense boundary where as soon as react hits a suspense boundary it realizes okay well I can send what I have so far"

**Monitoring Performance:**
- Use Network tab: "Show you a lot of these things in terms of how fast or how slow or just how large your resources are"
- Use Performance tab: "If you record and let's say I click around the site it profiles the site"
- Check Web Vitals: "LCP (Largest Contentful Paint)", "INP (Interaction to Next Paint)", "CLS (Cumulative Layout Shift)", "FCP (First Contentful Paint)", "TTFB (Time to First Byte)"

This represents a complete collection of all performance-related tips and concepts discussed in the transcript.
