import React from 'react'

import './placeholder.scss'

export default function Placeholder({description, isPassword = false}) {
    return (
      <div className='placeholder'>
          <input type={isPassword ? "password" : "text"} className="placeholder__field" required />
          <label className="placeholder__label">{description}</label>
      </div>
    )
}