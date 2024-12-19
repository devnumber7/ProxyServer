package main 

import (
  "errors"
  "fmt"
  "io"
  "net/http"
  "os"

)

func getRoot(w http.ResponseWriter, r *http.Request){
  fmt.Printf("got /request\n")
  io.WriteString(w, "This is toy server\n")
}

func getHello(w http.ResponseWriter, r *http.Request){
  fmt.Printf("got /request\n")
  io.WriteString(w, "HELLLLLLLOOOOOOOOOOOO")
}


func main() {
	http.HandleFunc("/", getRoot)      // Register the root handler
	http.HandleFunc("/hello", getHello) // Register the /hello handler

	fmt.Println("Starting server on :3333...")
	err := http.ListenAndServe(":3333", nil)
	if errors.Is(err, http.ErrServerClosed) {
		fmt.Printf("server closed\n")
	} else if err != nil {
		fmt.Printf("error starting server: %s\n", err)
		os.Exit(1)
	}
}
