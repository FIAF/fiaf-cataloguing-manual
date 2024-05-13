

// mission here is to create svg to disk, then worry about insertion

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
    .attr("width", 800)
    .attr("height", 500)
    .style("fill", "white");



const nodes = [


    {'top': 'hello', 'cla':'sab', 'lines': [
        {"text":"Sabrina","x":100, "y":50},
        {"text":"(1954) (Work)","x":100, "y":50}
    ]},

    {'top': 'hello','cla':'aud', 'lines': [
    
        {"text":"The Audrey Hepburn Collection","x":300, "y":50},
        {"text":"(2008) (Work)","x":300, "y":50}
    ]},



    {'top': 'hello', 'cla':'fun', 'lines': [
        {"text":"Funny Face","x":500, "y":50},
        {"text":"(1956) (Work)","x":500, "y":50}
    ]},
] 



nodes.forEach(
    d => { 
        
        
        
        
        console.log(d);
    
    
    
    
    



          svg.selectAll('g')
          .data(d['lines'])
          .join('text')
          .attr("class", d.cla) // class should be at box level
          .attr('x', d => d.x)
          .attr('y', (d,i) => (d.y)+(i*20))
          .attr('font-family', 'brownstd')
          .attr('font-size', '12px')
          .attr('font-weight', '100')
          .attr('text-anchor', 'middle')
          .attr('alignment-baseline', 'middle')
          .attr('stroke', 'black')
          .attr('fill', 'black')
          .text(d => d.text)
    })




    // console.log(d3.select('#sab').node())

//  get a bbox for each class

// nodes.forEach(d => 
//     { d.box = d3.select("#"+d.class).node().getBBox()}
// )
  

// console.log(nodes)


fs.writeFileSync('diagrams/E.5.1.1/en.svg', body.html());


