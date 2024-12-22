// !preview r2d3 data = NULL, css = "circle/style.css"
//

// Select the SVG
svg
  .attr('style', 'border: 1px solid black;');

// Append a circle to the SVG
const circle = svg.append('circle')
  .attr('cx', 200)
  .attr('cy', 150)
  .attr('r', 50)
  .attr('fill', 'blue');

// Create a tooltip div
const tooltip = d3.select('body')
  .append('div')
  .attr('class', 'tooltip');

// Add mouse event listeners
circle
  .on('mouseover', function (event) {
    tooltip
      .style('visibility', 'visible')
      .text('This is a blue circle!');
  })
  .on('mousemove', function (event) {
    tooltip
      .style('top', (event.pageY) + 'px')
      .style('left', (event.pageX) + 'px');
  })
  .on('mouseout', function () {
    tooltip.style('visibility', 'hidden');
  });
