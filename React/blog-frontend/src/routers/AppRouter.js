import React from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import { BlogPage } from '../components/BlogPage'
import { Footer } from '../components/Footer'
import { Header } from '../components/Header'

export const AppRouter = () => {

    return (
        <Router>
            <React.StrictMode>
                <Header/>
                <Switch>
                    <Route exact path='/' component={BlogPage}/>
                </Switch>
                <Footer/>
            </React.StrictMode>
        </Router>
    )
}