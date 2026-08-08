const VIDEO_ID = "eCHh-iVZW2Q";
const VIDEO_URL = `https://www.youtube.com/watch?v=${VIDEO_ID}`;
const THUMBNAIL = "./video-thumbnail.jpg";
const LOGO = "./lifeusa-logo-horizontal.png";

const variants = [
  { key: "A", name: "Cinematic song portrait" },
  { key: "B", name: "Split-screen song poster" },
  { key: "C", name: "Theatre listening room" },
];

const icons = {
  play: `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>`,
  arrow: `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"/></svg>`,
  share: `<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 10.5 6.8-4M8.6 13.5l6.8 4"/></svg>`,
};

let activeTransition;
let activeLyricsObserver;

function Header({ transparent = false } = {}) {
  return `
    <header class="site-header ${transparent ? "is-transparent" : ""}">
      <a class="brand" href="#top" aria-label="LIFE for Relief and Development home">
        <img src="${LOGO}" alt="LIFE for Relief and Development">
      </a>
      <nav aria-label="Campaign navigation">
        <a href="#story">Why it matters</a>
        <a href="#song">Hear the song</a>
        <a href="#lyrics">Read the lyrics</a>
        <a class="nav-cta" href="#take-action">Stand with Gaza's children</a>
      </nav>
    </header>`;
}

function VideoPoster({ label = "Play the song for Gaza", mode = "wide" } = {}) {
  return `
    <button class="video-poster video-${mode}" data-play-video type="button" aria-label="${label}">
      <img src="${THUMBNAIL}" alt="Still from LIFE's 60,000+ Orphans in Gaza music video">
      <span class="poster-scrim"></span>
      <span class="play-button">${icons.play}</span>
      <span class="poster-label">${label}</span>
    </button>`;
}

function ActionPair({ dark = false } = {}) {
  return `
    <div class="action-pair ${dark ? "on-dark" : ""}">
      <a class="button button-primary" href="#take-action">Stand with Gaza's children ${icons.arrow}</a>
      <a class="button button-ghost" href="${VIDEO_URL}" target="_blank" rel="noreferrer">Listen on YouTube</a>
    </div>`;
}

function EvidenceNote() {
  return `<p class="evidence-note"><strong>240,000+ views and counting.</strong> The song is reaching people around the world. Help it reach one more.</p>`;
}

function LyricsSection() {
  return `
    <section class="lyrics-section" id="lyrics" aria-labelledby="lyrics-title">
      <div class="lyrics-heading">
        <p class="section-kicker">Lyrics</p>
        <h2 id="lyrics-title">Words at the heart of the song.</h2>
        <p>Follow every word, then listen again.</p>
        <button class="lyrics-play" data-jump-video type="button">${icons.play}<span>Play the song</span></button>
      </div>
      <div class="lyrics-reading">
        <blockquote class="lyrics-refrain">
          <span>“60,000 orphans in Gaza.</span>
          <span>Don't look away.”</span>
        </blockquote>
        <div class="lyrics-transcript" aria-label="Complete lyrics">
          <div class="lyrics-column">
            <p class="lyrics-stanza">There’s a child dreaming tonight,<br>
              Holding on to a little light.<br>
              Waiting for someone to care,<br>
              Waiting to know someone’s there.<br>
              One small gift, one open heart,<br>
              Can help a brand-new future start.</p>

            <p class="lyrics-stanza lyrics-chorus">60,000 orphans in Gaza,<br>
              60,000 dreams to save.<br>
              60,000 orphans in Gaza,<br>
              Don’t look away,<br>
              don’t look away.<br>
              60,000 orphans in Gaza,<br>
              Waiting for hope today.<br>
              60,000 orphans in Gaza,<br>
              Be the change, be the change.<br>
              Ahhhhhhh. Ahhhhhhh.<br>
              Be the change</p>

            <p class="lyrics-stanza">A little love can go so far,<br>
              A little hope can heal the scars.<br>
              What you give today can shine,<br>
              In a child’s life for all time.</p>
          </div>

          <div class="lyrics-column">
            <p class="lyrics-stanza lyrics-chorus">60,000 orphans in Gaza,<br>
              60,000 dreams to save.<br>
              60,000 orphans in Gaza,<br>
              Don’t look away,<br>
              don’t look away.<br>
              60,000 orphans in Gaza,<br>
              60,000 dreams to save.<br>
              60,000 orphans in Gaza,<br>
              Don’t look away, ………..</p>

            <p class="lyrics-stanza lyrics-bridge">Sponsor an orphan today<br>
              through Life for Relief and Development.<br>
              Where there is life,<br>
              There is hope.<br>
              Sponsor an orphan today. …</p>

            <p class="lyrics-stanza lyrics-outro">60,000 orphans in Gaza<br>
              ooooooooh………<br>
              60,000 orphans in Gaza<br>
              Don’t look away,<br>
              don’t look away<br>
              60,000 orphans in Gaza,<br>
              Awaaaaaaaaaaaaaaay-<br>
              60,000 orphans in Gaza.<br>
              60,000 orphans in Gaza</p>
          </div>
        </div>
      </div>
    </section>`;
}

function Footer() {
  return `
    <footer class="site-footer">
      <div><strong>LIFE</strong><span>Life for Relief and Development</span></div>
      <p>Where there is life, there is hope.</p>
    </footer>`;
}

function VariantA() {
  return `
    <div class="variant variant-a" id="top">
      <section class="a-hero">
        ${Header({ transparent: true })}
        <img class="hero-image" src="${THUMBNAIL}" alt="">
        <div class="hero-wash"></div>
        <div class="a-hero-content">
          <p class="eyebrow">A song for the children of Gaza</p>
          <h1><span>60,000</span> Orphans in Gaza</h1>
          <p class="hero-deck">A child should be known by their dreams and the future still ahead of them, not by the loss they have endured. This song asks the world to listen and stand beside Gaza's orphaned children.</p>
          <div class="a-actions">
            <button class="round-play" data-jump-video type="button">${icons.play}<span>Play the song</span></button>
            ${ActionPair({ dark: true })}
          </div>
          <div class="view-proof" aria-label="More than 240,000 views and counting"><strong>240K+</strong><span>views and counting</span></div>
        </div>
      </section>

      <main id="main">
        <section class="a-statement" id="story">
          <p class="section-kicker">They are children before they are a number</p>
          <h2>War changed their childhoods. It must not define their futures.</h2>
          <div class="statement-grid">
            <p>Behind 60,000 are children living with a loss no child should have to carry. Each one still has a voice, a gift, and a future worth protecting.</p>
            <p class="pull-quote">“They are not a number to remember. They are children to stand beside.”</p>
          </div>
        </section>

        <section class="a-film" id="song">
          <div class="film-heading"><span>01</span><div><p>Listen to the official song</p><h2>Hear the song the world is carrying.</h2></div></div>
          ${VideoPoster({ label: "Play 60,000+ Orphans in Gaza", mode: "cinematic" })}
          ${EvidenceNote()}
        </section>

        ${LyricsSection()}

        <section class="a-action" id="take-action">
          <p class="section-kicker">Do not let the final note be the end</p>
          <h2>When the song ends, let compassion keep moving.</h2>
          <div class="action-steps">
            <article><span>01</span><h3>Listen</h3><p>Stay with the song from the first note to the last.</p></article>
            <article><span>02</span><h3>Share</h3><p>Send the song to someone who needs to hear it.</p></article>
            <article><span>03</span><h3>Stand with them</h3><p>Help LIFE keep Gaza's children seen, remembered, and supported.</p></article>
          </div>
          ${ActionPair()}
        </section>
      </main>
      ${Footer()}
    </div>`;
}

function VariantB() {
  return `
    <div class="variant variant-b" id="top">
      ${Header()}
      <main id="main">
        <section class="b-poster">
          <div class="b-poster-copy">
            <p class="eyebrow">A LIFE song for Gaza's children</p>
            <h1 aria-label="60,000 Orphans in Gaza"><span>60,000</span><br>Orphans<br>in Gaza</h1>
            <p class="b-poster-deck">One song. Thousands of childhoods changed by loss. A call to see every child beyond the number.</p>
            ${ActionPair()}
            <div class="b-poster-credit"><span>A story of loss, courage, and hope</span><span>Life for Relief and Development</span></div>
          </div>
          <div class="b-poster-visual">
            <img src="${THUMBNAIL}" alt="A child featured in LIFE's song for Gaza campaign">
            <button class="b-poster-play" data-jump-video type="button">${icons.play}<span>Play the song</span></button>
            <p>A child is more than what war has taken.</p>
          </div>
        </section>

        <section class="b-reel" id="song">
          <div class="b-reel-index" aria-hidden="true">
            <span>Press play</span><span>The official LIFE song</span><span>Share the song</span>
          </div>
          ${VideoPoster({ label: "Play 60,000+ Orphans in Gaza", mode: "poster" })}
          <div class="b-reel-caption">
            <strong>60,000+ Orphans in Gaza</strong>
            <p><strong>240,000+ views and counting.</strong> Every view is a chance for one more person to see the child behind the number.</p>
            <p class="evidence-note">Listen fully. Share it thoughtfully. Keep the story moving.</p>
          </div>
        </section>

        ${LyricsSection()}

        <section class="b-frames" id="story">
          <div class="b-frame-lead">
            <p class="section-kicker">Three ways to carry the story</p>
            <h2>Listen.<br>See them.<br>Stand with them.</h2>
          </div>
          <article><span>01</span><h3>Hear the song</h3><p>Give these children more than a passing moment.</p></article>
          <article><span>02</span><h3>See the child</h3><p>Every number holds a life, a memory, and a future.</p></article>
          <article><span>03</span><h3>Keep hope moving</h3><p>Share the song, then stand with Gaza's children through LIFE.</p></article>
        </section>

        <section class="b-endcard" id="take-action">
          <div><p class="section-kicker">The story continues</p><h2>The last note is not the end of their story.</h2></div>
          ${ActionPair()}
        </section>
      </main>
      ${Footer()}
    </div>`;
}

function VariantC() {
  return `
    <div class="variant variant-c" id="top">
      ${Header()}
      <main id="main">
        <section class="c-marquee">
          <p class="eyebrow">Now playing · A song the world is carrying</p>
          <h1>60,000 Orphans in Gaza</h1>
          <div class="c-marquee-line">
            <span>A song for Gaza's children</span><span>240,000+ views</span><span>Presented by LIFE</span>
          </div>
        </section>

        <section class="c-screen" id="song">
          <div class="c-screen-frame">
            ${VideoPoster({ label: "Play 60,000+ Orphans in Gaza", mode: "theatre" })}
          </div>
          <p class="c-screen-caption">Listen with sound. Stay with the song.</p>
        </section>

        ${LyricsSection()}

        <section class="c-credits" id="story">
          <p class="c-credit-label">When the song ends</p>
          <h2>Do not let their story fade with the final note.</h2>
          <div>
            <p>For Gaza's orphaned children, grief does not end when the music stops. But neither do courage, possibility, or the right to a future. Carry their story from attention to compassion, and from compassion to action.</p>
            <blockquote>“A child who has lost so much should never lose the world's attention.”</blockquote>
            <p class="evidence-note">More than 240,000 views have carried the song this far. Help carry it farther.</p>
          </div>
        </section>

        <section class="c-lobby" id="take-action">
          <div><p class="section-kicker">Turn attention into care</p><h2>Carry their story beyond the screen.</h2></div>
          ${ActionPair({ dark: true })}
        </section>
      </main>
      ${Footer()}
    </div>`;
}

function ApproachSwitcher(currentKey) {
  const current = variants.find((variant) => variant.key === currentKey) ?? variants[0];
  return `
    <aside class="prototype-switcher" aria-label="UI approach selector">
      <span class="prototype-badge">3 UI approaches</span>
      <button type="button" data-cycle="-1" aria-label="Previous UI approach">←</button>
      <div><strong>${current.key} — ${current.name}</strong><small>Use the arrows to compare all three</small></div>
      <button type="button" data-cycle="1" aria-label="Next UI approach">→</button>
    </aside>`;
}

function getVariant() {
  const key = new URLSearchParams(window.location.search).get("variant")?.toUpperCase();
  return variants.some((item) => item.key === key) ? key : "A";
}

function getEmbedMode() {
  return new URLSearchParams(window.location.search).get("embed") === "wix";
}

function cycleVariant(direction) {
  const current = getVariant();
  const index = variants.findIndex((item) => item.key === current);
  const next = variants[(index + direction + variants.length) % variants.length];
  const url = new URL(window.location.href);
  url.searchParams.set("variant", next.key);
  window.history.replaceState({}, "", url);
  renderWithTransition();
}

function mountVideo(target) {
  const frame = document.createElement("iframe");
  frame.className = target.className;
  frame.src = `https://www.youtube.com/embed/${VIDEO_ID}?autoplay=1&rel=0`;
  frame.title = "60,000+ Orphans in Gaza | LIFE campaign song";
  frame.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
  frame.referrerPolicy = "strict-origin-when-cross-origin";
  frame.allowFullscreen = true;
  target.replaceWith(frame);
  return frame;
}

function playCampaignSong() {
  const target = document.querySelector("#song [data-play-video]");
  const player = target ? mountVideo(target) : document.querySelector("#song iframe");
  player?.scrollIntoView({ behavior: "smooth", block: "center" });
}

async function shareCampaign() {
  const shareData = { title: "60,000 Orphans in Gaza", text: "LIFE's song for Gaza's orphaned children has been watched more than 240,000 times. Watch it and help carry their story forward.", url: VIDEO_URL };
  if (navigator.share) {
    try {
      await navigator.share(shareData);
    } catch (error) {
      if (error.name !== "AbortError") throw error;
    }
    return;
  }
  await navigator.clipboard.writeText(VIDEO_URL);
  const status = document.createElement("div");
  status.className = "toast";
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  status.textContent = "YouTube link copied";
  document.body.append(status);
  setTimeout(() => status.remove(), 2200);
}

function bindInteractions() {
  document.querySelectorAll("[data-cycle]").forEach((button) => button.addEventListener("click", () => cycleVariant(Number(button.dataset.cycle))));
  document.querySelectorAll("[data-play-video]").forEach((button) => button.addEventListener("click", () => mountVideo(button)));
  document.querySelectorAll("[data-jump-video]").forEach((button) => button.addEventListener("click", playCampaignSong));
  document.querySelectorAll("[data-share]").forEach((button) => button.addEventListener("click", shareCampaign));
}

function watchLyricsVisibility() {
  activeLyricsObserver?.disconnect();
  document.documentElement.classList.remove("lyrics-in-view");
  const lyrics = document.querySelector("#lyrics");
  if (!lyrics || !("IntersectionObserver" in window)) return;

  activeLyricsObserver = new IntersectionObserver(([entry]) => {
    document.documentElement.classList.toggle("lyrics-in-view", entry.isIntersecting);
  }, { rootMargin: "-12% 0px -12%", threshold: 0 });
  activeLyricsObserver.observe(lyrics);
}

function render({ animate = false } = {}) {
  const key = getVariant();
  const embedMode = getEmbedMode();
  const view = key === "B" ? VariantB() : key === "C" ? VariantC() : VariantA();
  const comparisonEnabled = !embedMode && (window.location.pathname.includes("/prototypes/") || window.location.pathname.includes("/songs-for-gaza-ui-approaches/") || ["localhost", "127.0.0.1"].includes(window.location.hostname));
  document.getElementById("app").innerHTML = view + (comparisonEnabled ? ApproachSwitcher(key) : "");
  if (animate) document.querySelector(".variant")?.classList.add("is-entering");
  document.documentElement.dataset.variant = key;
  document.documentElement.dataset.embed = embedMode ? "wix" : "standalone";
  bindInteractions();
  watchLyricsVisibility();
}

function renderWithTransition() {
  activeTransition?.skipTransition();
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!document.startViewTransition || reducedMotion) {
    render({ animate: true });
    window.scrollTo({ top: 0, behavior: "instant" });
    return;
  }

  activeTransition = document.startViewTransition(() => {
    render({ animate: true });
    window.scrollTo({ top: 0, behavior: "instant" });
  });
  activeTransition.finished.finally(() => {
    activeTransition = undefined;
  });
}

window.addEventListener("popstate", render);
window.addEventListener("keydown", (event) => {
  if (!["ArrowLeft", "ArrowRight"].includes(event.key)) return;
  if (event.target.matches("input, textarea, [contenteditable='true']")) return;
  event.preventDefault();
  cycleVariant(event.key === "ArrowRight" ? 1 : -1);
});

render();
