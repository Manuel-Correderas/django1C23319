const { createApp } = Vue;
  createApp( {data() {
    return { 
 
    url: 'https://manucorre88.pythonanywhere.com/productos',
    productos: [], // Inicializa la propiedad 'productos' como un arreglo vacío
    }
  },
  methods: {
    fetchData(url) {

        fetch(url)
            .then(response => response.json())
            .then(data => { 
                this.productos=data
                console.log((this.productos))
            })

    }
  },
  created(){

    this.fetchData(this.url) 
  }

  
}).mount('#app')