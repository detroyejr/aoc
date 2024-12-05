#' Day 02

puzzle_input <- function(file) {
  readLines(file) |>
    strsplit(split = "x") |>
    lapply(as.numeric) |>
    lapply(as.list) |>
    lapply(setNames, c("l", "w", "h"))
}

part1 <- function(x) {
  box <- sapply(x, function(x) with(x, 2 * l * w + 2 * w * h + 2 * h * l))
  extra <- sapply(x, function(e) prod(sort(unlist(e))[1:2]))
  sum(box + extra)
}

part2 <- function(x) {
  present <- sapply(x, function(e) sum(sort(unlist(e))[1:2] * 2))
  bow <- sapply(x, function(x) with(x, l * w * h))
  sum(present + bow)
}

x <- puzzle_input("inputs/02.txt")

cat("Part 1:", part1(x), "\n")
cat("Part 2:", part2(x), "\n")
