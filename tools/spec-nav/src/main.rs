use clap::{Parser, Subcommand};
use std::io::{self, Write};

#[derive(Parser)]
#[command(
    version,
    about = "Read-only Markdown navigation. Run from the project root."
)]
struct Cli {
    #[command(subcommand)]
    command: Command,
}

#[derive(Subcommand)]
enum Command {
    /// Show selection metadata and outgoing links; never open link targets.
    Map {
        #[arg(default_value = "docs/specs/README.md")]
        node: String,
    },
    /// Print the complete source byte-for-byte, even when selecting a fragment.
    Read { node: String },
    /// Follow only explicitly declared Markdown dependencies.
    Deps { node: String },
}

fn main() {
    let cli = Cli::parse();
    let result = std::env::current_dir()
        .map_err(|error| error.to_string())
        .and_then(|root| spec_nav::Project::new(&root))
        .map(|project| match cli.command {
            Command::Map { node } => project.map(&node),
            Command::Read { node } => project.read(&node),
            Command::Deps { node } => project.deps(&node),
        });
    let report = result.unwrap_or_else(spec_nav::Report::error);
    if let Err(error) = io::stdout().lock().write_all(report.output.as_bytes()) {
        eprintln!("spec-nav: {error}");
        std::process::exit(1);
    }
    for error in &report.errors {
        eprintln!("spec-nav: {error}");
    }
    if !report.errors.is_empty() {
        std::process::exit(1);
    }
}
