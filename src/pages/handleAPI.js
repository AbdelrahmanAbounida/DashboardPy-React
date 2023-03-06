import axios from 'axios'
import { useSelector } from 'react-redux'

const base_url = "https://aboneda2.pythonanywhere.com/api/"

  const SetData = ()=>{

    // general state
  const RevenueState = useSelector((state) => state.ExcelModel.Revenue)
  const OperationalCostState = useSelector((state) => state.ExcelModel.OperationalCost)
  const CapitalInvestmentState = useSelector((state) => state.ExcelModel.CapitalInvestment)
  const TimeLineState = useSelector((state) => state.ExcelModel.TimeLine)
  const OthersState = useSelector((state) => state.ExcelModel.Others)



  }
// Revenues
export const getRevenuesAPI = async ()=>{
    const revenues = await axios.get(`${base_url}revenues/`)
    console.log(revenues)
    return revenues
}
export const setRevenuesAPI = async (data)=>{
    for (const [key, value] of Object.entries(data)) {
        console.log(key, value);
      }
}
// operationalCosts
export const getOperationalCostAPI = async ()=>{
    const operationalCosts = await axios.get(`${base_url}operationalCosts/`)
    console.log(operationalCosts)
    return operationalCosts
}
// capital_investments
export const getCapitalInvestmentAPI = async ()=>{
    const capital_investments = await axios.get(`${base_url}capital_investments/`)
    console.log(capital_investments)
    return capital_investments
}
// timelines
export const getTimeLineAPI = async ()=>{
    const timelines = await axios.get(`${base_url}timelines/`)
    console.log(timelines)
    return timelines
}
// others
export const getOthersAPI = async ()=>{
    const others = await axios.get(`${base_url}others/`)
    console.log(others)
    return others
}