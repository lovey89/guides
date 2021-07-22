// Run this program with:
// go run . | cut -c 7- | base64 -d > pic.png; xdg-open pic.png

package main

import "golang.org/x/tour/pic"
import "image"
import "image/color"

type Image struct{}

func (i Image) ColorModel() color.Model {
	return color.RGBAModel
}

func (i Image) Bounds() image.Rectangle {
	return image.Rect(0, 0, 255, 255)
}

func (i Image) At(x, y int) color.Color {
	return color.NRGBA{uint8(x), uint8(y), uint8(x + y), uint8(((x+y)%255)/16 + 240)}
}

func main() {
	m := Image{}
	pic.ShowImage(m)
}
