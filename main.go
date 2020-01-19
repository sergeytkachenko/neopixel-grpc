package main

import (
	"bufio"
	"fmt"
	"io"
	"os/exec"
)

const PYTHON_FILE_NAME = "neopixel-interface.py"

func main() {
	cmd := exec.Command("python", PYTHON_FILE_NAME, "4", "100", "100", "255", "0.3")
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

func copyOutput(r io.Reader) {
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}
