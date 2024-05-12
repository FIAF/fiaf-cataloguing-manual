


var jsdom = require('jsdom');
const { JSDOM } = jsdom;
const d3 = require('d3');
const fs = require('fs');


const dom = new JSDOM(`<!DOCTYPE html>


<head>
    <title>FIAFcore</title>
  
    <link href="https://fonts.googleapis.com/css?family=Pacifico:100,200,300,400,500,600,700,800,900"
        rel="stylesheet" />

            <style>
        
              		@font-face{
          			font-family: "Brown";
          			src: url("./BrownStd-Regular.ttf") format("truetype");
          		}	
             </style>

</head>



<body></body>`);



let body = d3.select(dom.window.document.querySelector("body"))
let svg = body.append('svg').attr('width', 800).attr('height', 800).attr('xmlns', 'http://www.w3.org/2000/svg');


svg.append("rect")
    .attr("x", 10)
    .attr("y", 10)
    .attr("width", 500)
    .attr("height", 500)
    .style("fill", "lime");



        svg.selectAll('g')
          .data([''])
          .join('text')
          .attr("class", "entity_text2")
          .attr('x', d => 50)
          .attr('y', d => 50)
          .attr('font-family', 'Pacifico')
          .attr('font-size', '16px')
          .attr('font-weight', '100')
          .attr('text-anchor', 'middle')
          .attr('alignment-baseline', 'middle')
          .attr('stroke', 'orange')
          .attr('fill', 'orange')
          .text(d => "hallo")


          svg.selectAll('g')
          .data([''])
          .join('text')
          .attr("class", "entity_text2")
          .attr('x', d => 50)
          .attr('y', d => 150)
          .attr('font-family', 'brownstd')
          .attr('font-size', '16px')
          .attr('font-weight', '100')
          .attr('text-anchor', 'middle')
          .attr('alignment-baseline', 'middle')
          .attr('stroke', 'blue')
          .attr('fill', 'blue')
          .text(d => "hallo")

fs.writeFileSync('diagrams/E.5.1.1/en.svg', body.html());


