#' Day 01

puzzle_input <- function(file) {
  strsplit(readLines(file), "")[[1]]
}

part1 <- function(x) {
  sum(ifelse(x == "(", 1, -1))
}

part2 <- function(x) {
  which(cumsum(ifelse(x == "(", 1, -1)) < 0)[1]
}

x <- puzzle_input("inputs/01.txt")

cat("Part 1:", part1(x), "\n")
cat("Part 2:", part2(x), "\n")
