import React from 'react';
import './ProductCard.css';


export default function ProductCard({img,name,price,category}) {
    return (
        <div className='container'>
            <img src={img} alt=''></img>
            <div className='text_container'>
            <p>{name}</p>
            <p>{category}</p>
            <p>{price}</p>
            </div>
        </div>
    )
}
