library(r2d3)

r2d3(
  data = NULL, 
  script = '
    // Select the SVG
    svg
      .attr("width", 400) 
      .attr("height", 300) 
      .style("border", "1px solid black"); 

    // Append a circle to the SVG
    const circle = svg.append("circle")
      .attr("cx", 200)
      .attr("cy", 150)
      .attr("r", 50)
      .attr("fill", "blue");

    // Create a tooltip div
    const tooltip = d3.select("body")
      .append("div")
      .attr("class", "tooltip")
      .style("opacity", 0); 

    // Add mouse event listeners
    circle
      .on("mouseover", function(event, d) {
        tooltip.transition()
          .duration(200)
          .style("opacity", 0.9);
        tooltip.html("This is a blue circle!")
          .style("left", (event.pageX) + "px")
          .style("top", (event.pageY - 28) + "px");
      })
      .on("mouseout", function(d) {
        tooltip.transition()
          .duration(500)
          .style("opacity", 0);
      });
  ',
  css = '.tooltip {
  position: absolute;
  background: lightgray;
  padding: 5px;
  border-radius: 5px;
  font-size: 12px;
  visibility: hidden;
}
'
)
