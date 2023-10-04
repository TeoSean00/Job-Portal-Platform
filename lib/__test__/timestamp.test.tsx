// import { expect } from "@jest/globals";

// import { longDateTime } from "../utils";

// describe("longDateTime", () => {
//   beforeAll(() => {
//     jest.useFakeTimers().setSystemTime(new Date("2023-04-20T00:00:00+08:00"));
//   });

//   it("should format correctly when a date is provided", () => {
//     expect(longDateTime.format(new Date())).toEqual(
//       "Tuesday, 20 Apr 2023, 12:00 AM",
//     );
//     expect(
//       longDateTime.format(new Date("2023-04-20T00:00:00.000+08:00")),
//     ).toEqual("Tuesday, 20 Apr 2023, 12:00 AM");
//     expect(longDateTime.format(new Date("2023"))).toEqual(
//       "Friday, 01 Jan 2023, 12:00 AM",
//     );
//     expect(longDateTime.format(new Date("2023-04"))).toEqual(
//       "Thursday, 01 Apr 2023, 12:00 AM",
//     );
//     expect(longDateTime.format(new Date("2023-04-20"))).toEqual(
//       "Tuesday, 20 Apr 2023, 12:00 AM",
//     );
//   });

//   describe("when input date is in UTC time", () => {
//     it("should return SGT date and time when it is the same date in UTC and SGT", () => {
//       expect(longDateTime.format(new Date("2023-11-30T14:00:00.000Z"))).toEqual(
//         "Tuesday, 30 Nov 2023, 10:00 PM",
//       );
//       expect(longDateTime.format(new Date("2023-11-30T15:59:59.059Z"))).toEqual(
//         "Tuesday, 30 Nov 2023, 11:59 PM",
//       );
//     });

//     it("should return SGT date and time when it is midnight in SGT", () => {
//       expect(longDateTime.format(new Date("2023-11-30T16:00:00.000Z"))).toEqual(
//         "Wednesday, 01 Dec 2023, 12:00 AM",
//       );
//     });

//     it("should return SGT date and time when SGT is one day ahead of UTC", () => {
//       expect(longDateTime.format(new Date("2023-11-30T16:53:10.065Z"))).toEqual(
//         "Wednesday, 01 Dec 2023, 12:53 AM",
//       );
//       expect(longDateTime.format(new Date("2023-11-30T20:00:00.000Z"))).toEqual(
//         "Wednesday, 01 Dec 2023, 04:00 AM",
//       );
//     });
//   });
// });
