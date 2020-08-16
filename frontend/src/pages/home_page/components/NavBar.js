import React, { Component } from 'react';
import './NavBar.css';

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";
  

{/* <Router>
<Link to="product">Home</Link>
</Router> */}

export default class NavBar extends Component {



    render() {
        <Router>
        </Router>


        if (this.props.categories){
            this.links = [{id:0, name:'all'}].concat(this.props.categories).map((cat,ind)=>{
                return (
                        <Link path='product'>
                            <a onClick={this.props.handleClick} id={cat.id}  href="#">{cat.name}</a>
                        </Link>
                )
                
            });
        }
    else {
        this.links = null;
    }

        return (
            <nav>
                <div className="nav-links" >
                    {this.links}
                </div>
            </nav>
        )
    }
}
