package main

import (
	"fmt"
	"golang.org/x/tour/reader"
)

type ErrEOF []byte

func (e ErrEOF) Error() string {
	return fmt.Sprintf("End of file")
}

type MyReader struct{}

// TODO: Add a Read([]byte) (int, error) method to MyReader.
func (r MyReader) Read(b []byte) (int, error) {
	if b == nil || len(b) == 0 {
		err := ErrEOF(b)
		return 0, err
	}
	for i := 0; i < len(b); i++ {
		b[i] = 'A'
	}
	return len(b), nil
}

func main() {
	reader.Validate(MyReader{})
}
