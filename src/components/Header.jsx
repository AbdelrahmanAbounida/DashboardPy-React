import { Typography, Box, useTheme } from "@mui/material";
import { colorPalette } from "../theme/theme";

const Header = ({ title, subtitle }) => {
  const theme = useTheme();
  const colors = colorPalette(theme.palette.mode);
  return (
    <Box mb="30px">
      <Typography
        variant="h1"
        color={colors.grey[500]}
        fontWeight="bold"
        sx={{ m: "0 0 2px 0" }}
      >
        {title}
      </Typography>
      <Typography variant="h4" color={colors.greenAccent[500]} sx={{fontWeight:"bold"}}>
        {subtitle}
      </Typography>
    </Box>
  );
};

export default Header;