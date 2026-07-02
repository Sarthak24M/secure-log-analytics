import { Box } from "@mui/material";

import Navbar from "../components/Navbar";
import SummaryCard from "../components/SummaryCard";

function Dashboard() {

    return (

        <>

            <Navbar />

            <Box
                sx={{
                    display: "flex",
                    gap: 3,
                    padding: 4,
                    flexWrap: "wrap"
                }}
            >

                <SummaryCard
                    title="Total Events"
                    value={289}
                />

                <SummaryCard
                    title="Failed Logins"
                    value={5}
                />

                <SummaryCard
                    title="High Alerts"
                    value={5}
                />

                <SummaryCard
                    title="Password Changes"
                    value={1}
                />

                <SummaryCard
                    title="Privileged Commands"
                    value={8}
                />

            </Box>

        </>

    );
}

export default Dashboard;