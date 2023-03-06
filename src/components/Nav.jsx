import React from 'react'
import {  NavLink  } from 'react-router-dom';
import { openDrawer } from '../features/DrawerOpen/DrawerOpenSlice';
import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import {MdOutlineDarkMode,MdOutlineLightMode} from 'react-icons/md'
import {Stack, Paper, Typography,Button,useTheme, Box} from '@mui/material'
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import { AppBar } from '../const/const';
import { useSelector, useDispatch } from 'react-redux'
import {colorPalette,ColorModeContext} from '../theme/theme'
import { useContext } from 'react';
const Nav = () => {
    const open = useSelector((state) => state.DrawerOpen.value)
    const logo = useSelector((state) => state.LogoAppear.value)

    const dispatch = useDispatch()

    const theme = useTheme();
    const colors = colorPalette(theme.palette.mode);
    const modeContext = useContext(ColorModeContext)

  return (
    <AppBar position="fixed" open={open} >
        <Toolbar component={Paper} sx={{justifyContent:"space-between",backgroundColor:"secondary.dark"}}>

          <Stack direction="row" >
              <IconButton
                color="inherit"
                aria-label="open drawer"
                onClick={()=>{dispatch(openDrawer())}}
                edge="start"
                sx={{ mr: 2, ...(open && { display: 'none' }) }}
              >
                <MenuIcon sx={{fontSize:35,color:"#fff"}}/>
              </IconButton>

            <NavLink to={""}  style={{textDecoration:"none"}}><Typography variant="h3" sx={{color:"primary.dark",ml:1,mt:1,fontWeight:"bold", display:logo?'inherit':'none','&: hover':{color:"lightseagreen"}}}>Control Panel</Typography> </NavLink>
          </Stack>

          <Box sx={{display:"flex", gap:3}}>
              
          {/* <Button
            sx={{
              backgroundColor: colors.greenAccent[700],
              '&:hover':{backgroundColor: colors.greenAccent[600]},
              color: "#fff",
              fontSize: "14px",
              fontWeight: "bold",
              mt:0.5
            }}
            onClick = {()=>{download()}}
          >
            <DownloadOutlinedIcon sx={{ mr: "10px" }} />
            Download Report
          </Button> */}

              <IconButton onClick={modeContext.toggleColorMode}>
                {theme.palette.mode === "dark" ? 
                (<MdOutlineDarkMode />) : (<MdOutlineLightMode />)  
                }
            </IconButton>

          </Box>


        </Toolbar>
      </AppBar>
  )
}

export default Nav
