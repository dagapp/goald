import React from 'react'

import Progressbar from "@components/Utils/Progressbar"

import { template } from "./groupCards"
import './group.scss'

export default function Group() {
    const name = template['title']
    const description = template['description']

    const goals = template['goals']
    const tags =  template['tags']
    
    return (
        <div className="group">
            <div className="group__feed">    
                <div className="group__feed_goals">
                    <h2 className='group__feed_goals_title card-title'>Goals</h2>
                    <div className="group__feed_goals_cards">
                        {goals.map(goal => {
                            return (
                                <div key={goal.id} className="group__feed_goals_card">
                                    <h3>{goal.title}</h3>
                                    <Progressbar 
                                        daysLeft= {goal.daysLeft} 
                                        amount= {goal.amount}
                                        goal= {goal.goal}
                                        percentage= {goal.percentage}
                                    />
                                </div>
                            );
                        })}
                    </div>
                </div>

                <div className="group__feed_actions">
                    <div className="group__feed_actions_events">
                        <h2 className='card-title'>Events</h2>
                    </div>

                    <div className="group__feed_actions_reports">
                        <h2 className='card-title'>Reports</h2>
                    </div>
                </div>
            </div>

            <div className="group__info">
                <div className="group__info_about">
                    <div className="info-card">
                        <div className="info-card_banner"></div>
                        <div className="info-card_avatar"></div>
                        
                        {/* Should this be with .toString()??? */}
                        <div className="info-card_title card-title">{name}</div>
                        <div className="info-card_description">
                            <div className="info-card_description_icon">
                                <svg fill="#ECE7F4" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M21,2H3A1,1,0,0,0,2,3V21a1,1,0,0,0,1,1H21a1,1,0,0,0,1-1V3A1,1,0,0,0,21,2ZM4,4H20V6H4ZM20,20H4V8H20ZM6,12a1,1,0,0,1,1-1H17a1,1,0,0,1,0,2H7A1,1,0,0,1,6,12Zm0,4a1,1,0,0,1,1-1h5a1,1,0,0,1,0,2H7A1,1,0,0,1,6,16Z"/>
                                </svg>
                            </div>
                            <div className="info-card_description_content">{description}</div>
                        </div>
                        
                        <div className="info-card_tags">
                            <div className="info-card_tags_icon">
                                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M7.0498 7.0498H7.0598M10.5118 3H7.8C6.11984 3 5.27976 3 4.63803 3.32698C4.07354 3.6146 3.6146 4.07354 3.32698 4.63803C3 5.27976 3 6.11984 3 7.8V10.5118C3 11.2455 3 11.6124 3.08289 11.9577C3.15638 12.2638 3.27759 12.5564 3.44208 12.8249C3.6276 13.1276 3.88703 13.387 4.40589 13.9059L9.10589 18.6059C10.2939 19.7939 10.888 20.388 11.5729 20.6105C12.1755 20.8063 12.8245 20.8063 13.4271 20.6105C14.112 20.388 14.7061 19.7939 15.8941 18.6059L18.6059 15.8941C19.7939 14.7061 20.388 14.112 20.6105 13.4271C20.8063 12.8245 20.8063 12.1755 20.6105 11.5729C20.388 10.888 19.7939 10.2939 18.6059 9.10589L13.9059 4.40589C13.387 3.88703 13.1276 3.6276 12.8249 3.44208C12.5564 3.27759 12.2638 3.15638 11.9577 3.08289C11.6124 3 11.2455 3 10.5118 3ZM7.5498 7.0498C7.5498 7.32595 7.32595 7.5498 7.0498 7.5498C6.77366 7.5498 6.5498 7.32595 6.5498 7.0498C6.5498 6.77366 6.77366 6.5498 7.0498 6.5498C7.32595 6.5498 7.5498 6.77366 7.5498 7.0498Z" stroke="#ECE7F4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            
                            <div className="info-card_tags_content">
                                {tags.map(tag => {
                                    return (
                                        <div key={tag.id} className="info-card_tag">{tag.value}</div>
                                    );
                                })}
                            </div>
                        </div>
                    </div>
                </div>

                <div className="group__info_participants">
                    <h2 className='card-title'>Particitants</h2>
                    
                </div>
            </div>
        </div>
    )
}
