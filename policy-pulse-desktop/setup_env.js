/**
 * Policy Pulse Desktop - Environment Setup Script
 *
 * This script automates the setup of the Node.js environment for Policy Pulse Desktop.
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

function setupNodeEnvironment() {
  console.log('Setting up Node.js environment for Policy Pulse Desktop...');

  try {
    // Check if package.json exists
    if (!fs.existsSync('./package.json')) {
      console.error('✗ package.json not found');
      return false;
    }

    // Install dependencies
    console.log('Installing dependencies...');
    execSync('npm install', { stdio: 'inherit' });

    console.log('✓ Dependencies installed successfully');

    // Verify installation
    console.log('Verifying installation...');
    const packageJson = JSON.parse(fs.readFileSync('./package.json', 'utf8'));
    console.log(`✓ Package: ${packageJson.name}@${packageJson.version}`);

    return true;
  } catch (error) {
    console.error('✗ Failed to setup Node.js environment:', error.message);
    return false;
  }
}

function verifySetup() {
  console.log('Verifying Node.js setup...');

  try {
    // Check if required files exist
    const requiredFiles = ['package.json', 'node_modules'];
    for (const file of requiredFiles) {
      if (!fs.existsSync(file)) {
        console.error(`✗ Required file/directory missing: ${file}`);
        return false;
      }
    }

    console.log('✓ All required files present');

    // Try to run a basic check
    execSync('npm list', { stdio: 'ignore' });
    console.log('✓ npm dependencies verified');

    return true;
  } catch (error) {
    console.error('✗ Setup verification failed:', error.message);
    return false;
  }
}

function main() {
  console.log('Policy Pulse Desktop Environment Setup');
  console.log('=' .repeat(40));

  let success = true;

  // Setup Node.js environment
  if (!setupNodeEnvironment()) {
    success = false;
  }

  // Verify setup
  if (success && !verifySetup()) {
    success = false;
  }

  if (success) {
    console.log('\n✓ Setup completed successfully!');
    console.log('\nTo run the application:');
    console.log('  npm start');
    console.log('\nTo build for production:');
    console.log('  npm run build');
    console.log('\nTo run tests:');
    console.log('  npm test');
  } else {
    console.log('\n✗ Setup failed. Please check the error messages above.');
    process.exit(1);
  }

  return 0;
}

if (require.main === module) {
  process.exit(main());
}

module.exports = { setupNodeEnvironment, verifySetup };