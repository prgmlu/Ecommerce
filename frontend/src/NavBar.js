import React, { Component } from 'react';
import './NavBar.css';

export default class NavBar extends Component {



    render() {
        if (this.props.categories){
            this.links = [{id:0, name:'all'}].concat(this.props.categories).map((cat,ind)=>{
                return <a onClick={this.props.handleClick} id={cat.id}  href="#">{cat.name}</a>
                
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
