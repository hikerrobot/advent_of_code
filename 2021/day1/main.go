package main

import (
	"fmt"
	"io/fs"
	"os"
)

func main() {
	fmt.Println("hello world")
	isValidFilePath := fs.ValidPath("\\input`")

	fmt.Println("file path valid? ", isValidFilePath)

	_, err := os.ReadFile("input1")

	if err != nil {
		fmt.Println("error reading file")
	}
}
