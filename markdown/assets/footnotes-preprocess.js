/**
 * footnotes-preprocess.js
 *
 * Runs before Paged.js processes the document. Converts each Python
 * footnotes-extension <li> into an inline <span class="pdf-footnote"> placed
 * immediately after its <sup> reference inside the same paragraph.
 *
 * Why inline <span> (not <li> or a block element):
 *   Using a block element (<li>) inside a <p> triggers Chrome's "block in
 *   inline" splitting, which creates a ghost fragment of the <p> after the
 *   block. This ghost fragment renders as a blank line in the PDF even after
 *   Paged.js moves the footnote element to the footnote area.
 *
 * Why position:absolute on the <span> (see print.css span.pdf-footnote rule):
 *   float:footnote is processed by Paged.js but is unknown to Chrome; without
 *   extra CSS the span's text content would be visible inline and would
 *   inflate the paragraph before Paged.js moves it, cascading all footnotes
 *   to the last page of the section. position:absolute removes the span from
 *   the normal text flow without creating a block-in-inline split.
 *
 * Paged.js's ej() guard only checks nodeType===1, so absolutely-positioned
 * spans are still processed by float:footnote handling.
 */
(function relocateFootnotes() {
  var fnBlock = document.querySelector('div.footnote');
  if (!fnBlock) return;

  // Map fn:N → <li> for quick lookup
  var liMap = {};
  fnBlock.querySelectorAll('li[id^="fn:"]').forEach(function (li) {
    liMap[li.id] = li;
  });

  document.querySelectorAll('sup[id^="fnref:"]').forEach(function (sup) {
    // Python's footnotes extension suffixes back-references after the first as
    // "fnref:1:1", "fnref:1:2", etc.  These map to "fn:1:1" / "fn:1:2" which
    // have no matching <li>, so only the first reference gets an inline span.
    // Subsequent references keep their original <sup> but carry no footnote
    // body — acceptable behaviour for a print document.
    var fnId = sup.id.replace(/^fnref:/, 'fn:');
    var li = liMap[fnId];
    if (!li) return;

    // Build an inline <span> containing the footnote text
    var span = document.createElement('span');
    span.className = 'pdf-footnote';
    span.id = fnId;

    // Copy the content of the <li>'s paragraph, stripping the backref arrow
    var p = li.querySelector('p');
    var source = p || li;
    Array.from(source.childNodes).forEach(function (node) {
      if (node.nodeType === 1 && node.classList.contains('footnote-backref')) return;
      span.appendChild(node.cloneNode(true));
    });

    // Insert inline immediately after the <sup>, inside the same paragraph
    sup.parentNode.insertBefore(span, sup.nextSibling);
  });

  // Remove the now-redundant end-of-document footnote block
  fnBlock.parentNode.removeChild(fnBlock);
})();
