package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	wordSplit := strings.Fields(s)
	m := make(map[string]int)

	for _, word := range wordSplit {
		m[word]++
	}

	return m
}

func main() {
	wc.Test(WordCount)
}
