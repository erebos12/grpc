package main

import (
	"fmt"
	"log"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func main() {

	g := gin.Default()
	g.GET("/rest/mult/:a/:b", func(ctx *gin.Context) {
		a, err := strconv.ParseUint(ctx.Param("a"), 10, 64)
		if err != nil {
			ctx.JSON(http.StatusBadRequest, gin.H{"error": "Invalid Parameter A"})
			return
		}
		b, err := strconv.ParseUint(ctx.Param("b"), 10, 64)
		if err != nil {
			ctx.JSON(http.StatusBadRequest, gin.H{"error": "Invalid Parameter B"})
			return
		}
		result := a * b
		ctx.JSON(http.StatusOK, gin.H{"result": fmt.Sprint(result)})

	})

	if err := g.Run(":4444"); err != nil {
		log.Fatalf("Failed to run server: %v", err)
	}

}
