library(ggplot2)

args <- commandArgs(trailingOnly=TRUE)
output_file <- args[1]

# Sample plot using mtcars dataset

mtcars |>
  ggplot() +
  aes(x=wt, y=mpg) +
  geom_point()
ggsave(output_file)