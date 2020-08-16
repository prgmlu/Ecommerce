import React, { Component } from 'react';
import './HomePage.css';

import ProductCard from './ProductCard.js';
import NavBar from './NavBar.js';




class HomePage extends Component {

    constructor(props) {
      super(props);
      this.state = {
        products: null,
        categories: null,
        currentItems: null,
        activeSection: null,
      };
      this.handleClick = this.handleClick.bind(this);
    }
  
    handleClick(ev) {
      if (this.state.activeSection) {
        this.state.activeSection.classList.remove('active');
      }
      ev.target.classList.add('active');
      this.setState({ activeSection: ev.target });
      console.log(this.state.products);
      let newItems = (ev.target.innerText == 'all') ? this.state.products : this.state.products.filter(item => (ev.target.innerText == item.category));
  
      this.setState(
        { currentItems: newItems }
      )
    }
  
    componentDidMount() {
  
      // // fetch('https://c5642a65b634.ngrok.io/product/')
      fetch('http://127.0.0.1:8000/product/')
        .then(response => response.json())
        .then(products => {
          console.log(products);
          this.setState({ products: products, currentItems: products })
  
          console.log('pass');
        })
  
      // fetch('https://c5642a65b634.ngrok.io/category/')
      fetch('http://127.0.0.1:8000/category/')
        .then(response => response.json())
        .then(categories => {
          console.log(categories);
          this.setState({ categories: categories })
  
          console.log(categories);
        })
  
  
  
    }
  
  
    render() {
      const { currentItems } = this.state;
  
      return (<div className="HomePage">

        <NavBar categories={this.state.categories} handleClick={this.handleClick} activeSection={this.state.activeSection} />
        <div className='grid'>
          {currentItems ?
            (currentItems.map((item, ind) => {
              return (<ProductCard key={ind} price={item.price} img={item.img} name={item.name} category={item.category} />)
            }))
            : (<p>loading</p>)}
        </div>
  
      </div>);
    }
  
  }
  
  export default HomePage;
  