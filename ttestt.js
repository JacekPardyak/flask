// !preview r2d3 data=c(0.3, 0.6, 0.8, 0.95, 0.40, 0.20)
//
// r2d3: https://rstudio.github.io/r2d3
//

// Ensure D3.js is loaded dynamically
if (!window.d3) {
  const script = document.createElement("script");
  script.src = "https://d3js.org/d3.v7.min.js";
  document.head.appendChild(script);
}

// Wait until D3.js is fully loaded
setTimeout(() => {
  // header
  const header =  d3.select("#output-header")
    .text("D3.js Visualization");
/// ----------------------------------------------------------------------------    
let width = 320, height = 320;

// Create an SVG element
const svg = d3.select("#output-body")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("border", "1px solid black")
    .append("g")
    .attr("id", "wrapper")
    .attr("transform", "translate(0, 5)");

var data = {
	"name": "A1",
	"children": [
		{
			"name": "B1",
			"children": [
				{
					"name": "C1",
					"value": 100
				},
				{
					"name": "C2",
					"value": 300
				},
				{
					"name": "C3",
					"value": 200
				}
			]
		},
		{
			"name": "B2",
			"value": 200
		}
	]
};

var packLayout = d3.pack()
	.size([300, 300]);

var rootNode = d3.hierarchy(data)

rootNode.sum(function(d) {
	return d.value;
});

packLayout(rootNode);

d3.select('svg g')
	.selectAll('circle')
	.data(rootNode.descendants())
	.join('circle')
	.attr('cx', function(d) { return d.x; })
	.attr('cy', function(d) { return d.y; })
	.attr('r', function(d) { return d.r; })
  .style("fill", "#333")
  .style("opacity", "0.3")
  .style("stroke", "white");


  }, 1000);
  