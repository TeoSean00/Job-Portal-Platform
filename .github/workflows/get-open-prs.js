const { Octokit } = require("@octokit/rest");
const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN,
});

(async () => {
  try {
    const { data } = await octokit.pulls.list({
      owner: process.env.GITHUB_REPOSITORY.split("/")[0],
      repo: process.env.GITHUB_REPOSITORY.split("/")[1],
      state: "open",
    });
    const openPrs = data
      .map((pr) => `- [${pr.title}](${pr.html_url})`)
      .join("\n");
    console.log(openPrs);
  } catch (error) {
    console.error(error);
    process.exit(1);
  }
})();
