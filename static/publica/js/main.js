const { createApp } = Vue  //creo un objeto VUE llamdo createApp

  createApp({
    data() {
      return {
       
        url:'https://manucorre88.pythonanywhere.com/productos',
        productos:[]
      } 
    },   
    methods: {
      fetchData(url) {

          fetch(url)
              .then(response => response.json())
              .then(data => { 
                  this.productos=data
                  console.log(this.productos)
              })

      }
    },
    created(){

      this.fetchData(this.url) 
    }

    
  }).mount('#app')