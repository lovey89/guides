package main

import (
	"fmt"
	"golang.org/x/tour/tree"
)
// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int) {
	defer close(ch) // <- closes the channel when this function returns
	var walk func(t *tree.Tree)
	walk = func(t *tree.Tree) {
		if t == nil {
			return
		}
		walk(t.Left)
		ch <- t.Value
		walk(t.Right)
	}
	walk(t)
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {
	ch1 := make(chan int)
	ch2 := make(chan int)
	go Walk(t1, ch1)
	go Walk(t2, ch2)

	for i1:= range ch1 {
		i2, ok := <-ch2
		if !ok || ( i1 != i2 ) {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(Same(tree.New(1),tree.New(1)))
	fmt.Println(Same(tree.New(3),tree.New(4)))
}
