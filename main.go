package main

import (
	"bufio"
	"fmt"
	"io"
	"os/exec"
)

const PYTHON_FILE_NAME = "neopixel-interface.py"

func main() {
	pixelShow("3", "255", "255", "10", "0.4")
	pixelShow("4", "255", "255", "10", "0.4")
	pixelShow("6", "255", "255", "10", "0.4")
}

func copyOutput(r io.Reader) {
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}

func pixelShow(pixelIndex string, red string, green string, blue string, opacity string) {
	cmd := exec.Command("python", PYTHON_FILE_NAME, string(pixelIndex), red, green, blue, opacity)
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		panic(err)
	}
	stderr, err := cmd.StderrPipe()
	if err != nil {
		panic(err)
	}
	err = cmd.Start()
	if err != nil {
		panic(err)
	}

	go copyOutput(stdout)
	go copyOutput(stderr)
	cmd.Wait()
}
