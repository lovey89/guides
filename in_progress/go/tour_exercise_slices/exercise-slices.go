// Run this program with:
//go run . | cut -c 7- | base64 -d > pic.png; xdg-open pic.png

package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
	a := make([][]uint8, dy)
	for i := range a {
		a[i] = make([]uint8, dx)
	}

	for i := 0; i < dy; i++ {
		for j := 0; j < dx; j++ {
			// Try the different options
			//a[i][j] = uint8((i + j ) / 2)
			//a[i][j] = uint8(i * j)
			a[i][j] = uint8(i ^ j)
		}
	}
	return a
}

func main() {
	pic.Show(Pic)
}

