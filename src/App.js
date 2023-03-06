import './App.css';
import {MainHeader,Main} from './components/';
import React from 'react';
import {Container} from '@mui/material'
import { Route, Routes }from 'react-router-dom'
import {HomePage, ExcelModel } from './pages';
import {Nav} from './components';
import { useSelector } from 'react-redux';
import Excel from './pages/Excel';
import { useMode, ColorModeContext } from './theme/theme';
import {ThemeProvider,CssBaseline} from '@mui/material';

function App() {

  const open = useSelector((state) => state.DrawerOpen.value)
  const [theme, colorMode] = useMode()

  return (
    <ColorModeContext.Provider value={colorMode}>
        <ThemeProvider theme={theme}>
              <CssBaseline />
              <div className="App">
                
                <Main open={open} >
                  <Container  sx={{mt:9,ml:open? "13%" : "0"}}>
                    <Nav />
                  <Routes>
                      <Route path="/ExcelModelwebView" element={<MainHeader />} >
                        <Route path="/ExcelModelwebView" element={<HomePage />} />
                        <Route path="/ExcelModelwebView/excel_model" element={<ExcelModel />} />
                      </Route>
                  </Routes>
                  </Container>
                </Main>
              </div>
        </ThemeProvider>
      </ColorModeContext.Provider>
  );
}

export default App;
