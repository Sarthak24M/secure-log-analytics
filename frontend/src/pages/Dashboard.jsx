import { Box } from "@mui/material";
import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import SummaryCard from "../components/SummaryCard";
import { getSummary } from "../services/api";

function Dashboard() {
    const [summary, setSummary] = useState(null);


    useEffect(() => {

    async function fetchSummary() {

        try {

            const data = await getSummary();

            setSummary(data);

        }

        catch (error) {

            console.error(error);

        }

    }

    fetchSummary();

    }, []);

    if (!summary) {

    return <h2>Loading...</h2>;

    }




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
                value={summary.total_events}
            />

            <SummaryCard
                title="Failed Logins"
                value={summary.authentication_failures}
            />

            <SummaryCard
                title="High Alerts"
                value={summary.high_severity_alerts}
            />

            <SummaryCard
                title="Password Changes"
                value={summary.password_changes}
            />

            <SummaryCard
                title="Privileged Commands"
                value={summary.privileged_commands}
            />

            </Box>

        </>

    );
}

export default Dashboard;