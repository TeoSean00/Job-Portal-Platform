"use client";

import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "./ui/Table"
import React, { useState } from 'react';

const invoices = [
    {
        invoice: "INV001",
        paymentStatus: "Paid",
        totalAmount: "$250.00",
        paymentMethod: "Credit Card",
    },
    {
        invoice: "INV002",
        paymentStatus: "Pending",
        totalAmount: "$150.00",
        paymentMethod: "PayPal",
    },
    {
        invoice: "INV003",
        paymentStatus: "Unpaid",
        totalAmount: "$350.00",
        paymentMethod: "Bank Transfer",
    },
    {
        invoice: "INV004",
        paymentStatus: "Paid",
        totalAmount: "$450.00",
        paymentMethod: "Credit Card",
    },
    {
        invoice: "INV005",
        paymentStatus: "Paid",
        totalAmount: "$550.00",
        paymentMethod: "PayPal",
    },
    {
        invoice: "INV006",
        paymentStatus: "Pending",
        totalAmount: "$200.00",
        paymentMethod: "Bank Transfer",
    },
    {
        invoice: "INV007",
        paymentStatus: "Unpaid",
        totalAmount: "$300.00",
        paymentMethod: "Credit Card",
    },
]

type Role = {
    roleId: number;
    roleName: string;
    roleDescription: string;
    roleStatus: string
};

type RoleDataProps = {
    roleData: Role[];
};

export function RoleTable(data: RoleDataProps) {
    const [roleData, setRoleData] = useState(data.roleData);
    console.log(roleData);
    return (
        <Table>
            <TableCaption>A list of your recent invoices.</TableCaption>
            <TableHeader>
                <TableRow>
                    <TableHead className="w-[100px]">Role ID</TableHead>
                    <TableHead>Role Name</TableHead>
                    <TableHead>Description</TableHead>
                    {/* <TableHead className="text-right">Amount</TableHead> */}
                </TableRow>
            </TableHeader>
            <TableBody>
                {roleData.map((role) => (
                    // Add some logic here to show all roles if user is logged in as admin
                    role.roleStatus == 'active' ? (
                        <TableRow key={role.roleId}>
                            <TableCell className="font-medium">{role.roleId}</TableCell>
                            <TableCell>{role.roleName}</TableCell>
                            <TableCell className="text-ellipsis overflow-hidden">{role.roleDescription}</TableCell>
                            {/* <TableCell className="text-right">{invoice.totalAmount}</TableCell> */}
                        </TableRow>
                    ) : null
                ))}
            </TableBody>
        </Table>
    )
}
