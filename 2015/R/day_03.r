#' Day 03

puzzle_input <- function(file) {
  readLines(file) |>
    strsplit("") |>
    (\(x) x[[1]])()
}


house_locations <- function(x) {
  paste(
    c(0, cumsum(ifelse(x == "^", 1, ifelse(x == "v", -1, 0)))),
    c(0, cumsum(ifelse(x == ">", 1, ifelse(x == "<", -1, 0))))
  )
}

part1 <- function(x) {
  houses <- house_locations(x)
  sum(!duplicated(houses))
}

part2 <- function(x) {
  santa <- house_locations(x[seq_along(x) %% 2 == 0])
  robot <- house_locations(x[seq_along(x) %% 2 == 1])
  sum(!duplicated(c(santa, robot)))
}

x <- puzzle_input("inputs/03.txt")


cat("Part 1:", part1(x), "\n")
cat("Part 2:", part2(x), "\n")
