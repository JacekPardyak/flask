library(r2d3)
#viz <- r2d3(data=c(0.3, 0.6, 0.8, 0.95, 0.40, 0.20), script = "./D3.js/barchart.js")
viz <- r2d3(script = "bar-data-js.js")
viz
save_d3_html(viz, file = "bar-data-viz.html")
