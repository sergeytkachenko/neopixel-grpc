package main

import (
	"bufio"
	"fmt"
	"io"
	"os/exec"
)

const PYTHON_NEOPIXEL_SET_INTERFACE_FILE = "neopixel-set-interface.py"
const PYTHON_NEOPIXEL_SHOW_INTERFACE_FILE = "neopixel-show-interface.py"

func main() {
	setPixel("3", "255", "255", "10", "0.4")
	setPixel("4", "255", "255", "10", "0.4")
	setPixel("6", "255", "255", "10", "0.4")
	showPixels()
}

func copyOutput(r io.Reader) {
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}

func setPixel(pixelIndex string, red string, green string, blue string, opacity string) {
	cmd := exec.Command("python", PYTHON_NEOPIXEL_SET_INTERFACE_FILE, string(pixelIndex), red, green, blue, opacity)
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

func showPixels() {
	cmd := exec.Command("python", PYTHON_NEOPIXEL_SHOW_INTERFACE_FILE)
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
