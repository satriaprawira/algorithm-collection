//A Go Language file to make HTTP Request with Token Authentication
//Please make a new url and bearer to test in httpbin.org

package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	// Init the HTTP Url Request & Token Bearer (If Any)
	url := "https://httpbin.org/bearer"
	var bearer = "Bearer 19041997"
	var jsonStr = []byte(`{"name":"Open Source"}`)
  
  // Set Client HTTP Request
	req, err := http.NewRequest("GET", url, bytes.NewBuffer(jsonStr))
	req.Header.Set("Content-Type", "application/json")
	req.Header.Add("Authorization", bearer)

	// Client HTTP Post
	client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
	defer resp.Body.Close()
	
	// HTTP Response
	data, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(data))
	
}
