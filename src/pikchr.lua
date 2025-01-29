-- Pandoc filter to process code blocks with class "pikchr" containing
-- pikchr markup into SVG images.
--
-- * Assumes Fossil is present on the path.
-- * For HTML formats, you may alternatively use --self-contained
--
-- https://pandoc.org/lua-filters.html#converting-abc-code-to-music-notation

local function pikchr(markup)
    local svg = pandoc.pipe("fossil", {"pikchr"}, markup)
    return svg
end

function CodeBlock(block)
    if block.classes[1] == "pikchr" then
        local img = pikchr(block.text)
        local fname = pandoc.sha1(img) .. "." .. "svg"
        pandoc.mediabag.insert(fname, "image/svg+xml", img)
        return pandoc.Para{ pandoc.Image({pandoc.Str("pikchr diagram")}, fname) }
    end
end

