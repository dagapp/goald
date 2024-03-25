import React from 'react'

export default function Checkbox({description}) {
    return (
      <div className="checkbox">
          <input type="checkbox" className='checkbox__button'/>
          <span className='checkbox__description'>{description}</span>
      </div>
    )
  }

