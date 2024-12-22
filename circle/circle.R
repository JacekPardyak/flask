library(magrittr)

"<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>Interactive Circle with Tooltip</title>
  <link rel='stylesheet' href='style.css'>
  <script src='https://d3js.org/d3.v7.min.js'></script>
</head>
<body>
  <svg id='mySvg' width='400' height='400' style='border: 1px solid black;'></svg>
  <script src='script.js'></script>
</body>
</html>" %>% writeLines("index.html")

".tooltip {
  position: absolute;
  background: lightgray;
  padding: 5px;
  border-radius: 5px;
  font-size: 12px;
  visibility: hidden;
}" %>% writeLines("style.css")

"// Select the SVG
const svg = d3.select('#mySvg');

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
      .style('top', (event.pageY + 10) + 'px')
      .style('left', (event.pageX + 10) + 'px');
  })
  .on('mouseout', function () {
    tooltip.style('visibility', 'hidden');
  });" %>% writeLines("script.js")

"index.html" %>% 
  readLines(warn = FALSE) %>%
  paste(collapse = "\n") %>%
  display_html()
