import React, { Fragment } from 'react'

import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/ToolBar'
import Typography from '@material-ui/core/Typography'
import CssBaseline from '@material-ui/core/CssBaseline'
import { makeStyles } from '@material-ui/core/styles'

const useStyles = makeStyles((theme) => ({
    appBar: {
        borderBottom: `1px solid $(theme.palette.divider)`
    }
}))

export const Header = () => {

    const classes = useStyles();

    return (
        <Fragment>
            <CssBaseline />
            <AppBar 
                position='static'
                color='white'
                elevation={0}
                className={classes.appBar}
            />
            <Toolbar>
                <Typography variant='h6' color='inherit' noWrap>
                    BlogmeUp
                </Typography>
            </Toolbar>
        </Fragment>
    )
}
