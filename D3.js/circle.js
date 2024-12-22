// !preview r2d3 data = c(), css = "D3.js/style.css"
//


// Create an SVG container
svg
  .attr('id', 'mySvg')
  .attr('width', 400)
  .attr('height', 300)
  .attr('style', 'border: 1px solid black;');

// Append a circle
const circle = svg.append("circle")
      .attr("cx", 200)
      .attr("cy", 150)
      .attr("r", 50)
      .attr('fill', '#69b3a2');

// Create a tooltip div
const tooltip = d3.select("body")
      .append("div")
      .attr("class", "tooltip");

// Add mouse event listeners
circle
      .on("mouseover", function (event) {
        tooltip
          .style("visibility", "visible")
          .text("This is a blue circle!");
      })
      .on("mousemove", function (event) {
        tooltip
          .style("top", (event.pageY + 10) + "px")
          .style("left", (event.pageX + 10) + "px");
      })
      .on("mouseout", function () {
        tooltip.style("visibility", "hidden");
      });