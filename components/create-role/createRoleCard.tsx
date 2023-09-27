import type { ReactNode } from "react";

import React from "react";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

type SelectOption = {
  value: string;
  label: string;
};

type CreateRoleCardProps = {
  title?: string;
  description?: string;
  roleNamePlaceholder?: string;
  roleDescriptionPlaceholder?: string;
  departmentLabel?: string;
  selectOptions: SelectOption[];
  children?: ReactNode;
};

const CreateRoleCard: React.FC<CreateRoleCardProps> = ({
  title = "Role Creation",
  description = "Enter role descriptions below.",
  roleNamePlaceholder = "Name of Role",
  roleDescriptionPlaceholder = "Description of Role",
  departmentLabel = "Department",
  selectOptions,
  children,
}) => (
  <Card className="w-[350px]">
    <CardHeader>
      <CardTitle>{title}</CardTitle>
      <CardDescription>{description}</CardDescription>
    </CardHeader>
    <CardContent>
      <form>
        <div className="grid w-full items-center gap-4">
          <div className="flex flex-col space-y-1.5">
            <Label htmlFor="name">Role Name</Label>
            <Input id="roleName" placeholder={roleNamePlaceholder} />
          </div>
          <div className="flex flex-col space-y-1.5">
            <Label htmlFor="name">Role Description</Label>
            <Input
              id="roleDescription"
              placeholder={roleDescriptionPlaceholder}
            />
          </div>
          <div className="flex flex-col space-y-1.5">
            <Label htmlFor="department">{departmentLabel}</Label>
            <Select>
              <SelectTrigger id="department">
                <SelectValue placeholder="Select" />
              </SelectTrigger>
              <SelectContent position="popper">
                {selectOptions.map((option) => (
                  <SelectItem key={option.value} value={option.value}>
                    {option.label}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
          {children}
        </div>
      </form>
    </CardContent>
    <CardFooter className="flex justify-between">
      <Button variant="outline">Cancel</Button>
      <Button>Submit</Button>
    </CardFooter>
  </Card>
);

export default CreateRoleCard;
