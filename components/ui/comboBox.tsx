/* eslint-disable import/no-cycle */

"use client";

import { CaretSortIcon, CheckIcon } from "@radix-ui/react-icons";
import * as React from "react";

import { Button } from "@/components/ui";
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
} from "@/components/ui/command";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { cn } from "@/lib/utils";

type Item = {
  value: string;
  label: string;
};

type ComboboxProps = {
  items: Item[];
  placeholder: string;
  value: string;
  onChange: (value: string) => void;
};

export function Combobox({
  items,
  placeholder,
  value,
  onChange,
}: ComboboxProps) {
  const [open, setOpen] = React.useState(false);

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button
          aria-expanded={open}
          className={cn(
            "w-full justify-between",
            !value && "font-normal text-muted-foreground",
          )}
          role="combobox"
          variant="outline"
        >
          {value
            ? items.find((item) => item.value === value)?.label
            : placeholder}
          <CaretSortIcon className="ml-2 h-4 w-4 shrink-0 opacity-50" />
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-full p-0">
        <Command>
          <CommandInput className="h-9 " placeholder="Search item..." />
          <CommandEmpty>No item found.</CommandEmpty>
          <CommandGroup>
            {items.map((item) => (
              <CommandItem
                key={item.value}
                onSelect={() => {
                  onChange(item.value === value ? "" : item.value);
                  setOpen(false);
                }}
              >
                {item.label}
                <CheckIcon
                  className={cn(
                    "ml-auto h-4 w-4",
                    value === item.value ? "opacity-100" : "opacity-0",
                  )}
                />
              </CommandItem>
            ))}
          </CommandGroup>
        </Command>
      </PopoverContent>
    </Popover>
  );
}
